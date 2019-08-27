Name: 		swaybg
Version:	1.0
Release:	1%{?dist}
Summary:	Wallpaper tool for Wayland compositors

License:	MIT
URL:		https://github.com/swaywm/swaybg
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	scdoc
BuildRequires:	systemd-devel
BuildRequires:	cmake
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel

%description
%{summary}

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%doc
%license LICENSE
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1.gz

%changelog
* Sat Jun 22 2019 Chris Cowley <chris@cowley.tech> - 1.0.1
- initial packaging
- Initial packaging

