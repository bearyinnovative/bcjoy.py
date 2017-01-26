"""
    bcjoy.badge.bearychat
    ~~~~~~~~~~~~~~~~~~~~~

    Render BearyChat badge:

          left        right
         ------------------
        | BearyChat | 5/16 |
         ------------------
          ^~~~~~~~~   ^~~~
          |           |
          text        value

"""

_tmpl = '''
<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20">
  <rect rx="3" width="{total_width}" height="20" fill="#555"></rect>
  <rect rx="3"
        x="{left_width}"
        width="{left_width}"
        height="20"
        fill="{color}">
  </rect>
  <path d="M{left_width} 0h{sep_width}v20h-{sep_width}z"
        fill="{color}">
  </path>
  <g text-anchor="middle" font-family="Verdana" font-size="11">
    {text_text}
    {value_text}
  </g>
</svg>
'''

_text_tmpl = '''
    <text fill="#010101" fill-opacity=".3" x="{x}" y="15">{text}</text>
    <text fill="#fff" x="{x}" y="14">{text}</text>
'''

_padding = 8
_sep_width = 4
_color = '#85c158'


def width(text: str) -> int:
    return len(text) * 7


def render(text: str, value: str) -> str:
    """Render badge.

    Args:
        text: badge text
        value: badge value
    """
    left_width = _padding + width(text) + _sep_width
    right_width = _sep_width + width(value) + _padding

    text_text = _text_tmpl.format(
        x=left_width / 2,
        text=text
    )
    value_text = _text_tmpl.format(
        x=left_width + right_width / 2,
        text=value
    )
    badge = _tmpl.format(
        total_width=left_width + right_width, left_width=left_width,
        color=_color, sep_width=_sep_width,
        text_text=text_text, value_text=value_text
    )

    return badge
