%global tl_name gobble
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	More gobble macros for PlainTeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/gobble
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX package gobble includes several gobble macros not included in
the LaTeX kernel. These macros remove a number of arguments after them,
a feature regulary used inside other macros. This includes gobble macros
for optional arguments. The LaTeX package gobble-user provides these
macros at the user level, i.e. using names without @ so that these can
be used without \makeatletter and \makeatother. The same macros are
provided inside .tex files for use with plain-TeX or other TeX formats.
However, the gobble macros for optional macros require \@ifnextchar to
be defined.

