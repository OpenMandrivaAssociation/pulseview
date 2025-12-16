%define sourcedate 20251204
%define gitcommit af02198

# NOTE To update this package run package-source.sh in order to create a new source
# NOTE tarball from the latest upstream git master branch.
# NOTE The script will adjust sourcedate & gitcommit defines to match created tarball.
# NOTE You may have to reload this file to see the changed values.

# NOTE Using source tarball for Qt6 as latest upstream release is Qt5 which is EOL/OOM.

Name:		pulseview
Version:	0.5.0+git%{sourcedate}.%{gitcommit}
Release:	2
Summary:	PulseView is a Qt-based LA/scope/MSO GUI for sigrok
URL:		http://www.sigrok.org
License:	GPL-3.0-or-later
Group:		Productivity/Scientific
Source0:	%{name}-%{sourcedate}-%{gitcommit}.tar.zst
# Original upstream source
#Source0:	https://sigrok.org/download/source/%%{name}/%%{name}-%%{version}.tar.gz
# Alternative GH source
#SOurce0:	https://github.com/sigrokproject/pulseview/archive/%%{version}/%%{name}-%%{version}.tar.gz

#BuildSystem:	cmake
#BuildRequires:	atomic-devel
BuildRequires:	asciidoctor
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Linguist)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glibmm-2.68)
BuildRequires:	pkgconfig(libsigrok)		>= 0.5.0
BuildRequires:	pkgconfig(libsigrokcxx)		>= 0.5.0
BuildRequires:	pkgconfig(libsigrokdecode)	>= 0.5.0


%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

PulseView is a Qt-based LA/scope/MSO GUI for sigrok.

%prep
%autosetup -n %{name}-%{sourcedate}-%{gitcommit} -p1

%build
%cmake \
	-DQt5_FOUND=BOOL:FALSE \
	-DGLIBMM_2_4_FOUND=BOOL:FALSE \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

%files
%doc NEWS README HACKING
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.sigrok.PulseView.desktop
%{_datadir}/metainfo/org.sigrok.PulseView.appdata.xml
%{_datadir}/icons/hicolor/48x48/apps/pulseview.png
%{_datadir}/icons/hicolor/scalable/apps/pulseview.svg
%{_docdir}/%{name}/*
%{_mandir}/man1/%{name}.1*



