%define	name	pekwm
%define	version	0.1.10
%define	rel	1
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://pekwm.org/
Source0:	%{name}-%{version}.tar.bz2

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
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%configure	--enable-shape \
		--enable-xinerama \
		--enable-menus \
		--enable-keygrabber \
		--enable-harbour \
		--disable-debug \
		--disable-pcre

%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

# install themes
tar -jxf %SOURCE10 -C $RPM_BUILD_ROOT/%{_datadir}/%{name}/themes
tar -jxf %SOURCE11 -C $RPM_BUILD_ROOT/%{_datadir}/%{name}/themes

# startfile
%{__cat} > $RPM_BUILD_ROOT%{_bindir}/start%{name} << EOF
exec %{_bindir}/%{name}
EOF

chmod 755 $RPM_BUILD_ROOT%{_bindir}/start%{name}

# session file
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d
%{__cat} > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/30%{name} << EOF
NAME=%{name}
EXEC=%{_bindir}/start%{name}
DESC=%{name} window manager
SCRIPT:
exec %{_bindir}/start%{name}
EOF

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/30%{name}
%config(noreplace) %{_sysconfdir}/pekwm
%{_bindir}/start%{name}
%{_bindir}/%{name}
%{_datadir}/man/man1/pekwm.1.lzma
