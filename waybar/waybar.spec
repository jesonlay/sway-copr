# Steps for building git snapshot:
#  - uncomment and change gitdate (YYYYMMDD)
#  - set commit to desired commit hash
#  - bump Release

#global gitdate  20190808
%global commit   0.7.2

%global scommit  %(c=%{commit}; echo ${c:0:7})
%global gitrel   %{?gitdate:.%{gitdate}git%{scommit}}
%global gitver   %{?gitdate:-%{gitdate}git%{scommit}}

Name:           waybar 
Version:        0.7.2
Release:        1%{?gitrel}%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors 
License:        MIT
URL:            https://github.com/Alexays/Waybar
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz
Patch0:         0001-fix-tray-set-item_is_menu-for-libappindicator-applet.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47.0

BuildRequires:  fmt-devel >= 5.3.0
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput) 
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.3.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)

Recommends:     fontawesome-fonts

%description
%{summary}.

%prep
%autosetup -p 1 -n Waybar-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}

%changelog
* Sat Jun 22 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jun 14 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.9-1
- Update to 0.6.9

* Sat Jun 08 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.8-1
- Update to 0.6.8

* Fri May 31 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.7-1
- Update to 0.6.7

* Wed May 22 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.6-3
- Update to 0.6.6
- Remove version check from wayland-protocols dependency

* Sat May 18 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.5-1
- Update to 0.6.5

* Fri May 17 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.4-2
- Make fontawesome-fonts weak dependency.

* Fri May 17 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.4-1
- Update to 0.6.4

* Sun May 12 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.3-1
- Update to 0.6.3

* Fri May 10 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.2-1
- Update to 0.6.2

* Thu May 02 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Thu Apr 04 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Mar 21 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Mon Mar 11 2019 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.0-1
- Initial package

