from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Token,
)


class NoClownFiestaStyle(Style):
    background_color = "#151515"  # bg
    highlight_color = "#1e222a"  # accent_lighter_blue (selection-ish)
    default_style = ""

    _FG = "#E1E1E1"
    _BG = "#151515"
    _BLUE = "#BAD7FF"
    _GBL = "#7E97AB"  # gray_blue (used for keywords, titles, headers)
    _MGR = "#727272"  # medium_gray (comments)
    _LGR = "#AFAFAF"
    _MGB = "#A2B5C1"  # medium_gray_blue (strings)
    _CYAN = "#88afa2"
    _RED = "#b46958"
    _GRN = "#90A959"
    _YEL = "#F4BF75"
    _ORG = "#FFA557"
    _MAG = "#AA759F"

    styles = {
        # Base text
        Token: _FG,
        Text: _FG,
        Punctuation: _FG,
        # Comments (theme uses medium_gray)
        Comment: f"italic {_MGR}",
        Comment.Hashbang: f"italic {_MGR}",
        Comment.Multiline: f"italic {_MGR}",
        Comment.Single: f"italic {_MGR}",
        Comment.Special: f"noitalic {_MGR}",
        # Keywords (gray_blue)
        Keyword: f"bold {_GBL}",
        Keyword.Namespace: f"bold {_GBL}",
        Keyword.Declaration: f"bold {_GBL}",
        Keyword.Reserved: f"bold {_GBL}",
        Keyword.Type: f"bold {_GBL}",
        Keyword.Pseudo: _GBL,
        # Names / identifiers
        Name: _FG,
        Name.Variable: _FG,  # Variable = white
        Name.Function: _CYAN,  # Function = cyan
        Name.Class: _FG,  # Type = white
        Name.Builtin: _CYAN,
        Name.Attribute: _BLUE,
        Name.Tag: _BLUE,  # Tag = blue
        Name.Constant: _FG,  # Constant = white
        Name.Exception: _RED,  # Exception = red
        Name.Decorator: _CYAN,
        # Literals / numbers / strings
        Literal: _MGB,
        String: _MGB,  # String = medium_gray_blue
        String.Doc: f"italic {_MGR}",
        String.Escape: _YEL,
        Number: _RED,  # Number/Boolean/Float = red
        Number.Float: _RED,
        Number.Integer: _RED,
        # Operators
        Operator: _FG,  # Operator = white
        Operator.Word: f"bold {_GBL}",
        # Generics / headings / UI-ish
        Generic.Heading: f"bold {_BLUE}",
        Generic.Subheading: f"bold {_GBL}",
        Generic.Deleted: _RED,
        Generic.Inserted: _GRN,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: _MGR,
        Generic.Output: _LGR,
        Generic.Traceback: _RED,
        # Errors
        Error: f"bold {_RED}",
    }
