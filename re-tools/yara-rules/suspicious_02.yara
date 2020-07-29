rule suspicious_strings
{
strings:
  $a = "Synflooding" ascii wide nocase
  $b = "Portscanner" ascii wide nocase
  $c = "Keylogger" ascii wide nocase
condition:
  ($a or $b or $c)
}