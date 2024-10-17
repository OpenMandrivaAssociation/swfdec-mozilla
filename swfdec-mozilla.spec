%define version 0.8.2
%define major 0.8
%define rel 6

Name:		swfdec-mozilla
Version:	%version
Release:	%mkrel %rel 
Summary:	Mozilla compatible plugin for Flash rendering
Group:		Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	LGPLv2+
URL:		https://swfdec.freedesktop.org/
Source0:	http://swfdec.freedesktop.org/download/%name/%major/%{name}-%{version}.tar.gz
BuildRequires: swfdec-devel >= %{version}
BuildRequires: libalsa-devel gtk2-devel
Suggests:	gstreamer0.10-ffmpeg
Suggests:	gstreamer0.10-plugins-ugly
Conflicts:	flashplayer-plugin

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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-6mdv2011.0
+ Revision: 615055
- the mass rebuild of 2010.1 packages

* Fri Apr 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-5mdv2010.1
+ Revision: 535406
- partly "fix" #58746 (Flash plugin no longer works since upgrade)

* Fri Mar 26 2010 Frederic Crozat <fcrozat@mandriva.com> 0.8.2-4mdv2010.1
+ Revision: 527646
- reupload stable release

* Mon Jan 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-0mdv2010.1
+ Revision: 495698
- 0.9.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.8.2-2mdv2010.0
+ Revision: 445301
- rebuild

* Sun Nov 02 2008 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 299249
- New version 0.8.2

* Mon Sep 08 2008 Michael Scherer <misc@mandriva.org> 0.8.0-1mdv2009.0
+ Revision: 282632
- new version

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 258144
- update file list
- New version 0.7.4
- drop firefox-devel BR

* Thu Jun 26 2008 Michael Scherer <misc@mandriva.org> 0.7.2-1mdv2009.0
+ Revision: 229367
- new version

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 177090
- new release

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 0.5.90-1mdv2008.1
+ Revision: 161112
- New version 0.5.90

* Fri Dec 28 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5.5-2mdv2008.1
+ Revision: 138888
- Add common gstreamer plugins packages needed to play video as suggests

* Tue Dec 18 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5.5-1mdv2008.1
+ Revision: 132140
- Release 0.5.5

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2008.1
+ Revision: 110164
- New version 0.5.4

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 97882
- New version 0.5.3

* Fri Aug 24 2007 Michael Scherer <misc@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 71008
- version 0.5.2

* Sun Aug 05 2007 Michael Scherer <misc@mandriva.org> 0.5.1-2mdv2008.0
+ Revision: 58994
- rebuild cause it still requires old library

* Sat Aug 04 2007 Michael Scherer <misc@mandriva.org> 0.5.1-1mdv2008.0
+ Revision: 58758
- version 0.5.1

* Sat Jul 14 2007 Michael Scherer <misc@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 51924
- 0.5.0

* Wed Jun 13 2007 Funda Wang <fwang@mandriva.org> 0.4.5-1mdv2008.0
+ Revision: 38420
- should be makeinstall_std
- New version

* Mon Apr 30 2007 Michael Scherer <misc@mandriva.org> 0.4.4-1mdv2008.0
+ Revision: 19445
- upgrade to 0.4.4


* Fri Mar 16 2007 Michael Scherer <misc@mandriva.org> 0.4.2-1mdv2007.1
+ Revision: 144726
- fix build with newer firefox, with a quick hack
- upgrade to 0.4.2

* Tue Jan 16 2007 Michael Scherer <misc@mandriva.org> 0.4.1-1mdv2007.1
+ Revision: 109383
- new version 0.4.1

* Mon Jan 08 2007 Michael Scherer <misc@mandriva.org> 0.4.0-1mdv2007.1
+ Revision: 106108
- import swfdec-mozilla 0.4.0
- Create swfdec-mozilla

