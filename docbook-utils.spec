%include	/usr/lib/rpm/macros.perl
Summary:	Shell scripts to manage DocBook documents
Summary(pl):	Skrypty do obróbki dokumentów DocBook
Name:		docbook-utils
Version:	0.6.9
Release:	3
LIcense:	Eric Bischoff, Mark Galassi, Jochem Huhmann, Steve Cheng, and Frederik Fouvry; GPL 2.0
Group:		Applications/Publishing/SGML
Group(de):	Applikationen/Publizieren/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-@.patch
Patch1:		%{name}-roff_includes_in_man_pages.patch
Requires:	docbook-style-dsssl >= 1.49
Requires:	jadetex >= 2.5
BuildRequires:	autoconf
Obsoletes:	docbook2X
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These little scripts allow to convert easily DocBook files to other
formats (HTML, RTF, PostScript...), and to compare SGML files.

%description -l pl
Te ma³e skrypty pozwalaj± w prosty sposób konwertowaæ pliki DocBook do
innych formatów (HTML, RTF, PostScript...) i porównywaæ pliki SGML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT
%{__make} install \
	prefix=$DESTDIR%{_prefix} \
	mandir=$DESTDIR%{_mandir} \
	docdir=$DESTDIR%{_datadir}/doc

rm -f doc/HTML/Makefile*
rm -f doc/HTML/*.in

gzip -9nf NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/HTML
%attr(755,root,root) %{_bindir}/jw
%attr(755,root,root) %{_bindir}/docbook2*
%attr(755,root,root) %{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
%{_datadir}/sgml/docbook/utils-%{version}/backends/*
%{_datadir}/sgml/docbook/utils-%{version}/frontends/*
%{_datadir}/sgml/docbook/utils-%{version}/helpers/*
%{_mandir}/man1/*
%{_mandir}/man7/*
