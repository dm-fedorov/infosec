rule suspicious_strings
{
strings:
  $mz = {4D 5A}  
condition:
  ($mz at 0)
}