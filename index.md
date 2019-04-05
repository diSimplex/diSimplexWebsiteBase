---
layout: default
---

Welcome to the diSimplicial Reality Lab. At the moment you will find a 
series of [working draft]{% web papers:/workingDraft %} [documents]{% web 
papers:/ %} exploring a [Computational Foundations of Mathematics]{% web 
papers:paper/hi/hilbertsProgram.html %}. These working drafts are, at the 
moment, focused upon providing an initial implementation of the 
computational language JoyLoL.

JoyLoL is a [concatenative programming 
language](https://en.wikipedia.org/wiki/Concatenative_programming_language)[^1]
which is a fixed point of the semantics functor. As such, it provides its 
own semantics, and so can provide a foundation for Mathematics. One of the 
most important properties of the JoyLoL compiler is that it only compiles 
verified code. The JoyLoL compiler is a self-hosting compiler, this means 
that it verifies its own correctness by compiling itself. However to do 
this we need a [protoJoyLoL compiler]{% web 
papers:paper/pr/protoJoyLoL.html %}.

----

[^1]: For more on Concatenative programming languages, see:
      [Concatenative.org](http://concatenative.org/wiki/view/Concatenative%20language) 
      and [Concatenative @ C2 Wiki](http://wiki.c2.com/?ConcatenativeLanguage).
