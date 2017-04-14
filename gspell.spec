#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	gspell - a spell-checking library for GTK+
Summary(pl.UTF-8):	gspell - biblioteka sprawdzania pisowni dla GTK+
Name:		gspell
Version:	1.4.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gspell/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	90a63f1ff2340597125babc867bd888c
URL:		https://wiki.gnome.org/Projects/gspell
BuildRequires:	enchant-devel >= 1.6.0
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	gtk-doc >= 1.25
BuildRequires:	iso-codes >= 0.35
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	enchant >= 1.6.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.20
Requires:	iso-codes >= 0.35
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gspell is a spell-checking library for GTK+. It provides a flexible
API to implement the spell checking in a GTK+ application.


%description -l pl.UTF-8
gspell to biblioteka do sprawdzania pisowni dla GTK+. Udostępnia
elastyczne API do implementowania sprawdzania pisowni w aplikacjach
GTK+.

%package devel
Summary:	Header files for gspell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gspell
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enchant-devel >= 1.6.0
Requires:	glib2-devel >= 1:2.44
Requires:	gtk+3-devel >= 3.20

%description devel
Header files for gspell library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gspell.

%package static
Summary:	Static gspell library
Summary(pl.UTF-8):	Statyczna biblioteka gspell
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gspell library.

%description static -l pl.UTF-8
Statyczna biblioteka gspell.

%package apidocs
Summary:	API documentation for gspell library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gspell
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for gspell library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gspell.

%package -n vala-gspell
Summary:	Vala API for gspell library
Summary(pl.UTF-8):	API języka Vala do biblioteki gspell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-gspell
Vala API for gspell library.

%description -n vala-gspell -l pl.UTF-8
API języka Vala do biblioteki gspell.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgspell-1.la

%find_lang gspell-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gspell-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgspell-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgspell-1.so.1
%{_libdir}/girepository-1.0/Gspell-1.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgspell-1.so
%{_includedir}/gspell-1
%{_datadir}/gir-1.0/Gspell-1.gir
%{_pkgconfigdir}/gspell-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgspell-1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gspell-1.0

%files -n vala-gspell
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gspell-1.deps
%{_datadir}/vala/vapi/gspell-1.vapi
