%include	/usr/lib/rpm/macros.perl
Summary:	Shell scripts to manage DocBook documents.
Name:		docbook-utils
Version:	0.6.9
Release:	2
LIcense:	Eric Bischoff, Mark Galassi, Jochem Huhmann, Steve Cheng, and Frederik Fouvry; GPL 2.0
Group:		Applications/Publishing/SGML
Group(de):	Applikationen/Publizieren/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-@.patch
PAtch1:		%{name}-roff_includes_in_man_pages.patch
Requires:	docbook-style-dsssl >= 1.49
Requires:	jadetex >= 2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These little scripts allow to convert easily DocBook files to other
formats (HTML, RTF, PostScript...), and to compare SGML files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING TODO
%doc doc/HTML
%attr(755,root,root) %{_bindir}/jw
%attr(755,root,root) %{_bindir}/docbook2*
%attr(755,root,root) %{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
%{_datadir}/sgml/docbook/utils-%{version}/backends/*
%{_datadir}/sgml/docbook/utils-%{version}/frontends/*
%{_datadir}/sgml/docbook/utils-%{version}/helpers/*
%{_mandir}/man1/*
%{_mandir}/man7/*
