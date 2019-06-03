# ck-benchmarks!

This project has a dependency to [CK Project](https://github.com/ctuning/ck). The previous CK's installation is expected to run this module.

The programs that were used were extracted from the [Benchmarks repository](https://github.com/guilhermeleobas/Benchmarks/). Feel free to add more programs by doing a pull request.

Usage
=============
#### Pull the repository into CK as follow:


ck pull repo --url=https://github.com/clappis/ck-benchmarks

After the installation you can see the programs available as follow:
```
ck list ck-benchmarks:program:
```

You can compile and run the programs as follow:

```
ck compile program:bitbench-drop3
ck run program:bitbench-drop3
```

It's possible to use different compilers and flags optimizations. Consult the CK documentation to find more details.
