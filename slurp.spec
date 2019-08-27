Name: 		slurp
Version:	1.2.0
Release:	0%{?dist}
Summary:	Select a region in a Wayland compositor and print it to the standard output. 

License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	scdoc

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
%{_bindir}/slurp
%{_mandir}/man1/slurp.1.gz

%changelog
* Sat Jun 22 2019 Chris Cowley <chris@cowley.tech> - 1.2.0-0
- Build 1.2.0

