import os.path


def resolve_path(path):
    project_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(project_dir, path)