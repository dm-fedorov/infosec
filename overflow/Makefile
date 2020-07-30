prog4: prog4.c
	gcc prog4.c -o prog4 -g -fno-stack-protector -fno-builtin -z execstack
prog4_canary: prog4.c
	gcc prog4.c -o prog4_canary -g -fno-builtin -z execstack
