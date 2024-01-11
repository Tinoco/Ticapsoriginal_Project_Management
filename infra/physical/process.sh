dtrace -n 'syscall:::entry{@[execname] = count();}'
