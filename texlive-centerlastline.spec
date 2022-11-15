Name:		texlive-centerlastline
Version:	56644
Release:	1
Summary:	Paragraphs with last line centered, known as "Spanish" paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/centerlastline
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/centerlastline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/centerlastline.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/centerlastline.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides a command \centerlastline and an
environment centerlastline that typeset "Spanish" paragraphs,
that is paragraphs without indentation, and last line centered,
useful to finish a large paragraph of text at the end of
chapters, prologues, etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/centerlastline
%{_texmfdistdir}/tex/latex/centerlastline
%doc %{_texmfdistdir}/doc/latex/centerlastline

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
