rule suspicious_strings
{
strings:
  $a = "Synflooding"
  $b = "Portscanner"
  $c = "Keylogger"
condition:
  ($a or $b or $c)
}