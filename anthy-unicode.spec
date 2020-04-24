#
# Conditional build:
%bcond_without	emacs	# Emacs-compiled elisp

Summary:	A Japanese character input system library (with dictionary)
Summary(pl.UTF-8):	System wprowadzania znaków japońskich (ze słownikiem)
Name:		anthy-unicode
Version:	1.0.0.20191015
Release:	1
License:	LGPL v2+ (library), GPL (dictionary)
Group:		Libraries
#Source0Download: https://github.com/fujiwarat/anthy-unicode/releases
Source0:	https://github.com/fujiwarat/anthy-unicode/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c1b0281a28bf85dc4ff6189a54ef7c32
URL:		https://github.com/fujiwarat/anthy-unicode
%{?with_emacs:BuildRequires:	emacs}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Japanese character input system library (with dictionary).

%description -l pl.UTF-8
System wprowadzania znaków japońskich (ze słownikiem).

%package devel
Summary:	Header files for anthy-unicode libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek anthy-unicode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anthy-unicode libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek anthy-unicode.

%package static
Summary:	Static anthy-unicode libraries
Summary(pl.UTF-8):	Statyczne biblioteki anthy-unicode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static anthy-unicode libraries.

%description static -l pl.UTF-8
Statyczne biblioteki anthy-unicode.

%package -n emacs-anthy-unicode
Summary:	Emacs anthy-unicode package
Summary(pl.UTF-8):	Pakiet anthy-unicode dla Emacsa
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}
Requires:	emacs

%description -n emacs-anthy-unicode
Emacs anthy-unicode package.

%description -n emacs-anthy-unicode -l pl.UTF-8
Pakiet anthy-unicode dla Emacsa.

%prep
%setup -q

%build
%configure \
	--with-lispdir=%{_lispdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%if %{without emacs}
	EMACS=/bin/true
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libanthy*-unicode.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DIARY NEWS README.en doc/[!M]* doc/MISC
%lang(ja) %doc README
%attr(755,root,root) %{_bindir}/anthy-agent-unicode
%attr(755,root,root) %{_bindir}/anthy-dic-tool-unicode
%attr(755,root,root) %{_bindir}/anthy-morphological-analyzer-unicode
%attr(755,root,root) %{_libdir}/libanthy-unicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanthy-unicode.so.0
%attr(755,root,root) %{_libdir}/libanthydic-unicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanthydic-unicode.so.0
%attr(755,root,root) %{_libdir}/libanthyinput-unicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanthyinput-unicode.so.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/anthy-unicode.conf
%{_datadir}/anthy-unicode

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanthy-unicode.so
%attr(755,root,root) %{_libdir}/libanthydic-unicode.so
%attr(755,root,root) %{_libdir}/libanthyinput-unicode.so
%{_includedir}/anthy-unicode-1.0
%{_pkgconfigdir}/anthy-unicode.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libanthy-unicode.a
%{_libdir}/libanthydic-unicode.a
%{_libdir}/libanthyinput-unicode.a

%files -n emacs-anthy-unicode
%defattr(644,root,root,755)
%dir %{_lispdir}/anthy-unicode
%{_lispdir}/anthy-unicode/anthy*.el
%{_lispdir}/anthy-unicode/leim-list.el
%if %{with emacs}
%{_lispdir}/anthy-unicode/anthy*.elc
%{_lispdir}/anthy-unicode/leim-list.elc
%endif
