%include	/usr/lib/rpm/macros.perl
Summary:	Shell scripts to manage DocBook documents
Summary(pl):	Skrypty do obróbki dokumentów DocBook
Name:		docbook-utils
Version:	0.6.13
Release:	1
License:	Eric Bischoff, Mark Galassi, Jochem Huhmann, Steve Cheng, and Frederik Fouvry; GPL 2.0
Group:		Applications/Publishing/SGML
Source0:	ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%{name}-%{version}.tar.gz
# Source0-md5: af785716b207a7a562551851298a3b1a
Source1:	gdp-both.dsl
Source2:	db2html
Patch1:		%{name}-roff_includes_in_man_pages.patch
Patch2:		%{name}-catalog.patch
URL:		http://sources.redhat.com/docbook-tools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	openjade >= 1.4-12.20020409
Requires:	docbook-style-dsssl >= 1.76-6
Requires:	jadetex >= 2.5
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
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/HTML/Makefile*
rm -f doc/HTML/*.in

install %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
sed 's/^ "USletter"/ "A4"/' %{SOURCE1} > $RPM_BUILD_ROOT/%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils-a4.dsl

for util in dvi html pdf ps rtf man texi tex ; do
	ln -sf docbook2${util} $RPM_BUILD_ROOT/%{_bindir}/db2${util}
	echo '.so jw.1' >$RPM_BUILD_ROOT/%{_mandir}/man1/db2${util}.1
done

install -m755 %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/db2html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO doc/HTML
%attr(755,root,root) %{_bindir}/jw
%attr(755,root,root) %{_bindir}/docbook2*
%attr(755,root,root) %{_bindir}/db2*
%attr(755,root,root) %{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}
%{_mandir}/man1/*
%{_mandir}/man7/*
