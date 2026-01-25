Use the [script](https://www.man7.org/linux/man-pages/man1/script.1.html) tool
to record your terminal session to a file:

1. Start recording
```
> script --log-out ~/.terminal_log 
Script started, output log file is '/home/sj/.terminal_log'.
```

2. Do your thing
```
> nvim
```

3. To stop recording press Ctrl-D (end of file)
```
> <Ctrl-D>
Script done.
```

4. Run the python script to filter out missing characters:
```
> python find_missing.py ~/.terminal_log
	0xf502
	0xf002
	0xea8c
	0xf426
	0xe348
	0xf022
> ```
