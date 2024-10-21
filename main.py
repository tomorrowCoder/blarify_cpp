from Graph.ProjectGraphCreator import ProjectGraphCreator
from LSP import LspCaller
from ProjectFilesIterator import ProjectFilesIterator


def main():
    lsp_caller = LspCaller()
    project_files_iterator = ProjectFilesIterator(
        "/home/juan/devel/blar/lsp-poc/",
        paths_to_skip=[
            "/home/juan/devel/blar/lsp-poc/__pycache__",
            "/home/juan/devel/blar/lsp-poc/.git",
            "/home/juan/devel/blar/lsp-poc/.venv",
            "/home/juan/devel/blar/lsp-poc/Graph/__pycache__",
            "/home/juan/devel/blar/lsp-poc/Graph/Node/__pycache__",
            "/home/juan/devel/blar/lsp-poc/Graph/Relationship/__pycache__",
            "/home/juan/devel/blar/lsp-poc/LSP/__pycache__",
        ],
    )

    graph_creator = ProjectGraphCreator("Test", lsp_caller, project_files_iterator)

    graph = graph_creator.build()
    print(graph)


if __name__ == "__main__":
    main()
