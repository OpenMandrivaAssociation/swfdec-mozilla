%define version 0.9.2
%define major 0.9
%define rel 0

Name:		swfdec-mozilla
Version:	%version
Release:	%mkrel %rel 
Summary:	Mozilla compatible plugin for Flash rendering
Group:		Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	LGPLv2+
URL:		http://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%major/%{name}-%{version}.tar.gz
BuildRequires: swfdec-devel >= %{version}
BuildRequires: libalsa-devel gtk2-devel
Suggests:	gstreamer0.10-ffmpeg
Suggests:	gstreamer0.10-plugins-ugly

%description
This is a Mozilla compatible plugin for rendering of Flash animations
based on the swfdec library. It should work as well in other browsers.

%prep
%setup -q 

%build
%configure2_5x --enable-shared --disable-static --with-plugin-dir=%{_libdir}/mozilla/plugins
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
%{_iconsdir}/hicolor/*/apps/*
