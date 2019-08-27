Name: 		swaylock
Version:	1.4
Release:	0%{?dist}
Summary:	Screen locker for Wayland

License:	MIT
URL:		https://github.com/swaywm/swaylock
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	pam-devel
BuildRequires:	libxkbcommon-devel
BuildRequires:	scdoc
BuildRequires:	git

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
%{_bindir}/swaylock
%{_mandir}/man1/swaylock.1.gz
/etc/pam.d/swaylock
/usr/share/bash-completion/completions/swaylock
/usr/share/fish/completions/swaylock.fish
/usr/share/zsh/site-functions/_swaylock

%changelog
* Sat Jun 22 2019 Chris Cowley <chris@cowley.tech> - 1.4-0
- Build 1.4
