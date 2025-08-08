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
    Other,
    Punctuation,
    String,
    Text,
    Token,
    Whitespace,
)


class NoClownFiestaStyle(Style):
    _fg = "#E1E1E1"
    _bg = "#151515"
    _alt_bg = "#171717"
    _accent = "#202020"
    _white = "#E1E1E1"
    _gray = "#373737"
    _medium_gray = "#727272"
    _light_gray = "#AFAFAF"
    _blue = "#BAD7FF"
    _gray_blue = "#7E97AB"
    _medium_gray_blue = "#A2B5C1"
    _cyan = "#88afa2"
    _red = "#b46958"
    _green = "#90A959"
    _yellow = "#F4BF75"
    _orange = "#FFA557"
    _cursor_fg = "#151515"
    _cursor_bg = "#D0D0D0"
    _error = "#984936"
    _accent_lighter_blue = "#1e222a"

    name = "no_clown_fiesta"
    aliases = ["no_clown_fiesta", "noclownfiesta", "no-clown-fiesta"]
    default_style = ""

    background_color = _bg
    highlight_color = _accent_lighter_blue
    line_number_color = _medium_gray
    line_number_background_color = _alt_bg
    line_number_special_color = _white
    line_number_special_background_color = _accent

    styles = {
        Text: _fg,
        Token: _fg,
        Whitespace: _light_gray,
        Error: f"bold {_error}",
        Other: _fg,

        Comment: _medium_gray,

        Keyword: _gray_blue,
        Keyword.Namespace: _red,

        Name: _white,
        Name.Builtin: _cyan,
        Name.Decorator: _cyan,
        Name.Exception: _red,
        Name.Function: _cyan,
        Name.Tag: _blue,
        Name.Class: _cyan,
        Name.Attribute: _cyan,

        Literal: _white,

        String: _medium_gray_blue,
        String.Char: _green,

        Number: _red,

        Operator: _white,
        Operator.Word: _gray_blue,
        Punctuation: _white,

        Generic.Deleted: _error,
        Generic.Inserted: _cyan,
        Generic.Error: f"bold {_error}",
        Generic.Output: _light_gray,
        Generic.Prompt: _blue,
        Generic.Subheading: _blue,
        Generic.Traceback: _error,
    }
