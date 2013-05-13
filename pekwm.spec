Name:		pekwm
Version:	0.1.12
Release:	3
URL:		http://pekwm.org/
Source0:	http://www.pekwm.org/projects/pekwm/files/%{name}-%{version}.tar.gz

# modify config
Source1:	pekwm_config
Source2:	pekwm_mouse

# add themes (fonts changed for Mandriva)
Source10:	Opus3_Alpha-dev-20050227.tar.bz2
Source11:	OpusOS-Deep.tar.bz2

License:	GPL
Group:		Graphical desktop/Other
Summary:	A minimalist window manager for the X Window System
Requires:	xterm
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	jpeg-devel
BuildRequires:	png-devel

%description
Pekwm is a window manager based on aewm++, but it no longer
resembles it. It is highly configurable, rather fast, and
aimed towards being usable while remaining pretty enough to
look at. Features include client window grouping into one
window frame, automatic window size, location, grouping
and title rewriting.

%prep
%setup -q

# modify config
cp -f %SOURCE1 data/config
cp -f %SOURCE2 data/mouse

%build
autoreconf -fi
%configure2_5x	--enable-shape \
		--enable-xinerama \
		--enable-menus \
		--enable-harbour \
		--disable-debug

%make

%install
%makeinstall_std

# install themes
tar -jxf %SOURCE10 -C %{buildroot}/%{_datadir}/%{name}/themes
tar -jxf %SOURCE11 -C %{buildroot}/%{_datadir}/%{name}/themes

# startfile
%{__cat} > %{buildroot}%{_bindir}/start%{name} << EOF
exec %{_bindir}/%{name}
EOF

chmod 755 %{buildroot}%{_bindir}/start%{name}

# session file
%{__install} -d %{buildroot}%{_sysconfdir}/X11/wmsession.d
%{__cat} > %{buildroot}%{_sysconfdir}/X11/wmsession.d/30%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

%files
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/30%{name}
%config(noreplace) %{_sysconfdir}/pekwm
%{_bindir}/start%{name}
%{_bindir}/%{name}
%{_datadir}/man/man1/pekwm.1*


%changelog
* Wed Sep 15 2010 Rémy Clouard <shikamaru@mandriva.org> 0.1.12-1mdv2011.0
+ Revision: 578754
- bump to final 0.1.12

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 0.1.12-0.rc1.1mdv2010.1
+ Revision: 518738
- New version 0.1.12 rc1

* Tue May 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.11-1mdv2010.0
+ Revision: 379988
- Update to new version 0.1.11

* Tue Jan 27 2009 Jérôme Soyer <saispo@mandriva.org> 0.1.10-1mdv2009.1
+ Revision: 334116
- New upstream release

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.1.9a-1mdv2009.1
+ Revision: 324513
- New upstream release

* Tue Aug 26 2008 Jérôme Soyer <saispo@mandriva.org> 0.1.7-1mdv2009.0
+ Revision: 276172
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.6-1mdv2008.1
+ Revision: 97353
- New release 0.1.6
- import pekwm


* Mon Apr 18 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.1.5-1mdk
- new release
- remove two themes (incompatible to pekwm-0.1.5)

* Mon Apr 17 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.1.4-1mdk
- new release
- remove Patch0 (pekwm-0.1.3-manpath.patch.bz2)
- (merged upstream)
- add requires xterm
- modify config
- add themes

* Tue Jul 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.1.3-4mdk
- rebuild
- fix summary-ended-with-dot
- %%mkrel

* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.3-3mdk
- rebuild for new g++

* Wed Mar 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.3-2mdk
- fix permissions (reported by Chris Moore <chris.moore@mail.com>)

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.3-1mdk
- initial mdk release
