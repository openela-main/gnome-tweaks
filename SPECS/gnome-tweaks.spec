%global majorversion %(cut -d "." -f 1-2 <<<%{version})

Name:           gnome-tweaks
Version:        3.28.1
Release:        7%{?dist}
Summary:        Customize advanced GNOME 3 options

# Software is GPLv3, Appdata file is CC0-1.0
License:        GPLv3 and CC0
URL:            https://wiki.gnome.org/action/show/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/%{majorversion}/%{name}-%{version}.tar.xz
Patch0:         reflect-extensions-status.patch
Patch1:         0001-extensions-Fix-opening-system-installed-extensions-i.patch
Patch2:         0002-settings-Drop-override-settings-support.patch
Patch3:         drop-app-menu-option.patch
Patch4:         extension-enable-state.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
Requires:       gnome-desktop3
Requires:       gnome-settings-daemon
Requires:       gnome-shell >= 3.24
Requires:       gnome-shell-extension-user-theme
Requires:       gobject-introspection
Requires:       gsettings-desktop-schemas >= 3.27.90
Requires:       gtk3 >= 3.12
Requires:       libnotify
Requires:       libsoup
Requires:       mutter
Requires:       pango
Requires:       python3dist(pygobject)
Provides:       gnome-tweak-tool = %{version}.%{release}
Obsoletes:      gnome-tweak-tool < 3.27.3-4
BuildArch:      noarch

%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-tweak-tool/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-tweak-tool/b.png

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/
%{_bindir}/%{name}
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{python3_sitelib}/gtweak/
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
* Tue Feb 18 2020 Milan Crha <mcrha@redhat.com> - 3.28.1-7
- extensions: Incorrectly shows enabled extensions as disabled after enable-all
- Resolves: #1804123

* Thu Jul 04 2019 Milan Crha <mcrha@redhat.com> - 3.28.1-6
- top-bar: Drop ApplicationMenu tweak
- Resolves: #1726656

* Tue Jul 02 2019 Milan Crha <mcrha@redhat.com> - 3.28.1-5
- settings: Drop override settings support
- Resolves: #1725741

* Tue Jun 18 2019 Milan Crha <mcrha@redhat.com> - 3.28.1-4
- extensions: Fix opening system installed extensions in gnome-software
- Resolves: #1721575

* Fri Apr 26 2019 Carlos Soriano <csoriano@redhat.com> - 3.28.1-3
- Fix reflect extension status in the UI
- Resolves: #1679127

* Tue Apr 23 2019 Carlos Soriano <csoriano@redhat.com> - 3.28.1-2
- Reflect extension status in the UI
- Resolves: #1679127

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.27.92-1
- Initial RPM release, based on gnome-tweak-tool.spec
