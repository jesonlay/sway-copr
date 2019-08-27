Name: 		swayidle
Version:	1.3
Release:	0%{?dist}
Summary:	Idle management daemon for Wayland

License:	MIT
URL:		https://github.com/swaywm/swayidle
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	scdoc
BuildRequires:	systemd-devel
BuildRequires:	cmake

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
%{_bindir}/swayidle
%{_mandir}/man1/swayidle.1.gz
/usr/share/bash-completion/completions/swayidle
/usr/share/fish/completions/swayidle.fish
/usr/share/zsh/site-functions/_swayidle

%changelog
* Sat Jun 22 2019 Chris Cowley <chris@cowley.tech> - 1.4-0
- Build 1.3

