%define version 0.5.2
%define rel 1

Name:		swfdec-mozilla
Version:	%version
Release:	%mkrel %rel 
Summary:	Mozilla compatible plugin for Flash rendering
Group:		Networking/WWW
License:	LGPL
URL:		http://swfdec.freedesktop.org/
Source:		http://swfdec.freedesktop.org/download/%name/%major/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: swfdec-devel >= 0.5.2
BuildRequires: libalsa-devel gtk2-devel
BuildRequires: mozilla-firefox-devel
%description
This is a Mozilla compatible plugin for rendering of Flash animations
based on the swfdec library. It should work as well in other browsers.

%prep
%setup -q 

%build
perl -pi -e 's/MOZILLA_DIR=mozilla-firefox/MOZILLA_DIR=mozilla/' ./configure.ac 
autoconf
export CFLAGS="%optflags -DMOZ_X11"
# some hack to make it compile, see with mrl after 2007.1 is out to see what would be the correct correction
# (misc)
export MOZILLA_CFLAGS="$(pkg-config --cflags firefox-plugin) $(pkg-config  --cflags firefox-plugin | awk '{print $1}' | sed 's|/[^/]*$||')" 
%configure2_5x --enable-shared 
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std 
rm -f $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/libswfdecmozilla.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/libswfdecmozilla.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/mozilla/plugins/libswfdecmozilla.so*
