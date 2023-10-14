import os
import sys
from logging import getLogger, basicConfig, INFO
from importlib.abc import MetaPathFinder


SEPARATOR = "."
basicConfig(level=INFO, format="%(message)s")
logger = getLogger(__name__)
sys_path_not_logged = True
EXCLUDE_DIRS = ("tests",)


def found_same_name(dirpath: str) -> bool:
    return os.path.isfile(f"{dirpath}.py")


def found_similar(module: str, dirpath: str, name: str) -> bool:
    module_path = module.replace(SEPARATOR, "/")
    abs_path = os.path.join(dirpath, name)
    if module_path in abs_path:
        logger.info(f"Something similar to '{module}' is found in '{abs_path}'.")
        return True
    return False


def search_neighbors(module: str) -> None:
    for sys_path_dir in sys.path:
        parent_directory = os.path.dirname(sys_path_dir)
        try:
            list_dir = os.listdir(sys_path_dir)
        except FileNotFoundError as e:
            logger.error(e)
            break

        child_directories = [
            os.path.join(sys_path_dir, d)
            for d in list_dir
            if os.path.isdir(os.path.join(sys_path_dir, d))
        ]
        for search_dir in [parent_directory] + child_directories:
            for dirpath, dirnames, files in os.walk(search_dir):
                if any(
                    [
                        exclude_dir
                        for exclude_dir in EXCLUDE_DIRS
                        if exclude_dir in dirpath
                    ]
                ):
                    continue
                if found_same_name(dirpath=dirpath):
                    logger.error(
                        f"'{module}' is not recognized as a package "
                        f"because '{dirpath}.py' exists. "
                    )
                    return
                for dirname in dirnames:
                    if found_similar(module=module, dirpath=dirpath, name=dirname):
                        return
                for file in files:
                    if found_similar(module=module, dirpath=dirpath, name=file):
                        return
    logger.error(f"Something similar to {module} is not found.")


def find(module: str):
    logger.info(f"Searching {module} ...")

    parent_module = SEPARATOR.join(module.split(SEPARATOR)[:-1])
    parent_spec = find(module=parent_module) if parent_module else None
    submodule_search_locations = (
        parent_spec.submodule_search_locations if parent_spec else None
    )

    finder: MetaPathFinder
    for finder in sys.meta_path:
        global sys_path_not_logged
        if (
            sys_path_not_logged
            and hasattr(finder, "__name__")
            and finder.__name__ == "PathFinder"
        ):
            logger.info(f"sys.path: {sys.path}")
            sys_path_not_logged = False
        try:
            target_spec = finder.find_spec(
                fullname=module, path=submodule_search_locations, target=None
            )
        except KeyError:
            logger.error(f"'{module}' is not recognized as a package.")
            exit()

        if target_spec:
            logger.info(f"'{module}' is found by {finder.__name__}.")
            break

    if not target_spec:
        logger.error(f"'{module}' is not found.")
        search_neighbors(module=module)
        exit()

    return target_spec


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        find(module=args[1])
    else:
        logger.info(
            "Please set a module path in the parameter, such as 'datetime.datetime'."
        )
