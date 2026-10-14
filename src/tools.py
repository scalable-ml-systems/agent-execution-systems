from dataclasses import dataclass
from pathlib import Path


@dataclass
class ToolResult:
    success: bool
    data: object | None = None
    error: str | None = None


LOG_DIRECTORY = Path("sample_data/logs")


def list_files() -> ToolResult:
    try:
        files = [
            item.name
            for item in LOG_DIRECTORY.iterdir()
            if item.is_file()
        ]

        files.sort()

        return ToolResult(
            success=True,
            data=files,
        )

    except Exception as exc:
        return ToolResult(
            success=False,
            error=str(exc),
        )


def read_file(filename: str) -> ToolResult:
    try:
        if Path(filename).name != filename:
            return ToolResult(
                success=False,
                error="Only filenames inside the log directory are allowed.",
            )

        file_path = LOG_DIRECTORY / filename

        if not file_path.is_file():
            return ToolResult(
                success=False,
                error=f"File not found: {filename}",
            )

        contents = file_path.read_text()

        return ToolResult(
            success=True,
            data=contents,
        )

    except Exception as exc:
        return ToolResult(
            success=False,
            error=str(exc),
        )

TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
}

if __name__ == "__main__":
    tool_name = "read_file"

    tool_function = TOOLS[tool_name]

    result = tool_function("database.log")

    print(list_files())
    print(read_file("database.log"))
    print(result)
