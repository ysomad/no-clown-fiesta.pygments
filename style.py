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
    _purple = "#AA749F"
    _magenta = "#AA759F"
    _cursor_fg = "#151515"
    _cursor_bg = "#D0D0D0"
    _sign_add = "#586935"
    _sign_change = "#51657B"
    _sign_delete = "#984936"
    _error = "#984936"
    _warning = "#ab8550"
    _info = "#ab8550"
    _hint = "#576f82"
    _todo = "#578266"
    _accent_lighter_blue = "#1e222a"
    _accent_blue = "#18191b"
    _accent_green = "#181b18"
    _accent_red = "#1b1818"

    name = "no_clown_fiesta"
    aliases = ["no_clown_fiesta", "noclownfiesta", "no-clown-fiesta"]
    web_style_gallery_exclude = False

    background_color = _bg
    highlight_color = _accent_lighter_blue

    line_number_color = _medium_gray
    line_number_background_color = _alt_bg
    line_number_special_color = _white
    line_number_special_background_color = _accent

    styles = {
        Text: _fg,
        Token: _fg,
        Comment: f"italic {_medium_gray}",
        Generic.Prompt: _gray,
        Generic.Output: _light_gray,
        Generic.Traceback: _error,
        Keyword: _gray_blue,
        Keyword.Type: _white,
        Operator: _white,
        Punctuation: _white,
        Name: _white,
        Name.Function: _cyan,
        Name.Class: _cyan,
        Name.Builtin: _cyan,
        Name.Variable: _white,
        Name.Constant: _white,
        Name.Attribute: _cyan,
        Name.Tag: _blue,
        String: _medium_gray_blue,
        String.Char: _gray_blue,
        Number: _red,
        Literal: _white,
        Literal.Date: _white,
        Generic.Heading: f"bold {_blue}",
        Generic.Subheading: f"bold {_blue}",
        Generic.Deleted: _red,
        Generic.Inserted: _green,
        Generic.Error: f"bold {_error}",
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Error: f"bg:{_bg} {_error}",
    }
