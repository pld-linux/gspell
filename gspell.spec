#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	gspell - a spell-checking library for GTK+
Summary(pl.UTF-8):	gspell - biblioteka sprawdzania pisowni dla GTK+
Name:		gspell
Version:	1.14.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/gspell/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	282c1ed7213a657e47de663fd2a081db
URL:		https://wiki.gnome.org/Projects/gspell
BuildRequires:	enchant2-devel >= 2.2
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.20
BuildRequires:	gtk-doc >= 1.25
BuildRequires:	libicu-devel
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	enchant2 >= 2.2
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.20
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
Requires:	enchant2-devel >= 2.2
Requires:	glib2-devel >= 1:2.44
Requires:	gtk+3-devel >= 3.20
Requires:	libicu-devel

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
BuildArch:	noarch

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
BuildArch:	noarch

%description -n vala-gspell
Vala API for gspell library.

%description -n vala-gspell -l pl.UTF-8
API języka Vala do biblioteki gspell.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Dinstall_tests=false

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang gspell-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gspell-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gspell-app1
%attr(755,root,root) %{_libdir}/libgspell-1.so.3
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
%{_gtkdocdir}/gspell-1

%files -n vala-gspell
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gspell-1.deps
%{_datadir}/vala/vapi/gspell-1.vapi
