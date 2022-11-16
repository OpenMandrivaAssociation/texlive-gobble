Name:		texlive-gobble
Version:	64967
Release:	1
Summary:	More gobble macros for PlainTeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gobble
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gobble.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX package gobble includes several gobble macros not
included in the LaTeX kernel. These macros remove a number of
arguments after them, a feature regulary used inside other
macros. This includes gobble macros for optional arguments. The
LaTeX package gobble-user provides these macros at the user
level, i.e. using names without @ so that these can be used
without \makeatletter and \makeatother. The same macros are
provided inside .tex files for use with plain-TeX or other TeX
formats. However, the gobble macros for optional macros require
\@ifnextchar to be defined.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/gobble
%{_texmfdistdir}/tex/generic/gobble
%doc %{_texmfdistdir}/doc/generic/gobble

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
