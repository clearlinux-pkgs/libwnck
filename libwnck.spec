#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwnck
Version  : 2.31.0
Release  : 21
URL      : https://download.gnome.org/sources/libwnck/2.31/libwnck-2.31.0.tar.xz
Source0  : https://download.gnome.org/sources/libwnck/2.31/libwnck-2.31.0.tar.xz
Summary  : Window Navigator Construction Kit library
Group    : Development/Tools
License  : LGPL-2.0
Requires: libwnck-bin = %{version}-%{release}
Requires: libwnck-data = %{version}-%{release}
Requires: libwnck-lib = %{version}-%{release}
Requires: libwnck-license = %{version}-%{release}
Requires: libwnck-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libXres-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(x11)

%description
libwnck
=======
libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%package bin
Summary: bin components for the libwnck package.
Group: Binaries
Requires: libwnck-data = %{version}-%{release}
Requires: libwnck-license = %{version}-%{release}

%description bin
bin components for the libwnck package.


%package data
Summary: data components for the libwnck package.
Group: Data

%description data
data components for the libwnck package.


%package dev
Summary: dev components for the libwnck package.
Group: Development
Requires: libwnck-lib = %{version}-%{release}
Requires: libwnck-bin = %{version}-%{release}
Requires: libwnck-data = %{version}-%{release}
Provides: libwnck-devel = %{version}-%{release}
Requires: libwnck = %{version}-%{release}

%description dev
dev components for the libwnck package.


%package doc
Summary: doc components for the libwnck package.
Group: Documentation

%description doc
doc components for the libwnck package.


%package lib
Summary: lib components for the libwnck package.
Group: Libraries
Requires: libwnck-data = %{version}-%{release}
Requires: libwnck-license = %{version}-%{release}

%description lib
lib components for the libwnck package.


%package license
Summary: license components for the libwnck package.
Group: Default

%description license
license components for the libwnck package.


%package locales
Summary: locales components for the libwnck package.
Group: Default

%description locales
locales components for the libwnck package.


%prep
%setup -q -n libwnck-2.31.0
cd %{_builddir}/libwnck-2.31.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664159115
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664159115
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwnck
cp %{_builddir}/libwnck-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libwnck/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
%make_install
%find_lang libwnck

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wnck-urgency-monitor
/usr/bin/wnckprop

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Wnck-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libwnck-1.0/libwnck/application.h
/usr/include/libwnck-1.0/libwnck/class-group.h
/usr/include/libwnck-1.0/libwnck/libwnck.h
/usr/include/libwnck-1.0/libwnck/pager.h
/usr/include/libwnck-1.0/libwnck/screen.h
/usr/include/libwnck-1.0/libwnck/selector.h
/usr/include/libwnck-1.0/libwnck/tasklist.h
/usr/include/libwnck-1.0/libwnck/util.h
/usr/include/libwnck-1.0/libwnck/version.h
/usr/include/libwnck-1.0/libwnck/window-action-menu.h
/usr/include/libwnck-1.0/libwnck/window.h
/usr/include/libwnck-1.0/libwnck/wnck-enum-types.h
/usr/include/libwnck-1.0/libwnck/workspace.h
/usr/lib64/libwnck-1.so
/usr/lib64/pkgconfig/libwnck-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libwnck/WnckApplication.html
/usr/share/gtk-doc/html/libwnck/WnckClassGroup.html
/usr/share/gtk-doc/html/libwnck/WnckPager.html
/usr/share/gtk-doc/html/libwnck/WnckScreen.html
/usr/share/gtk-doc/html/libwnck/WnckSelector.html
/usr/share/gtk-doc/html/libwnck/WnckTasklist.html
/usr/share/gtk-doc/html/libwnck/WnckWindow.html
/usr/share/gtk-doc/html/libwnck/WnckWorkspace.html
/usr/share/gtk-doc/html/libwnck/core.html
/usr/share/gtk-doc/html/libwnck/home.png
/usr/share/gtk-doc/html/libwnck/index.html
/usr/share/gtk-doc/html/libwnck/index.sgml
/usr/share/gtk-doc/html/libwnck/indexes.html
/usr/share/gtk-doc/html/libwnck/intro.html
/usr/share/gtk-doc/html/libwnck/ix01.html
/usr/share/gtk-doc/html/libwnck/ix02.html
/usr/share/gtk-doc/html/libwnck/ix03.html
/usr/share/gtk-doc/html/libwnck/ix04.html
/usr/share/gtk-doc/html/libwnck/ix05.html
/usr/share/gtk-doc/html/libwnck/ix06.html
/usr/share/gtk-doc/html/libwnck/ix07.html
/usr/share/gtk-doc/html/libwnck/ix08.html
/usr/share/gtk-doc/html/libwnck/ix09.html
/usr/share/gtk-doc/html/libwnck/ix10.html
/usr/share/gtk-doc/html/libwnck/ix11.html
/usr/share/gtk-doc/html/libwnck/ix12.html
/usr/share/gtk-doc/html/libwnck/ix13.html
/usr/share/gtk-doc/html/libwnck/left.png
/usr/share/gtk-doc/html/libwnck/libwnck-Miscellaneous-Functions.html
/usr/share/gtk-doc/html/libwnck/libwnck-Resource-Usage-of-X-Clients.html
/usr/share/gtk-doc/html/libwnck/libwnck-Version-Information.html
/usr/share/gtk-doc/html/libwnck/libwnck-Window-Action-Menu.html
/usr/share/gtk-doc/html/libwnck/libwnck.devhelp2
/usr/share/gtk-doc/html/libwnck/right.png
/usr/share/gtk-doc/html/libwnck/style.css
/usr/share/gtk-doc/html/libwnck/up.png
/usr/share/gtk-doc/html/libwnck/utils.html
/usr/share/gtk-doc/html/libwnck/widgets.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwnck-1.so.22
/usr/lib64/libwnck-1.so.22.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwnck/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f libwnck.lang
%defattr(-,root,root,-)

