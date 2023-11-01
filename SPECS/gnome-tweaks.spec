%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d '.' -f 1 <<<%{tarball_version})

Name:           gnome-tweaks
Version:        40.10
Release:        1%{?dist}
Summary:        Customize advanced GNOME 3 options

# Software is GPLv3, Appdata file is CC0-1.0
License:        GPLv3 and CC0
URL:            https://wiki.gnome.org/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
Requires:       gnome-desktop3
Requires:       gnome-settings-daemon
Requires:       gnome-shell
Requires:       gnome-shell-extension-user-theme
Requires:       gnome-themes-extra
Requires:       gobject-introspection
Requires:       gsettings-desktop-schemas
Requires:       gtk3
Requires:       libhandy1
Requires:       libnotify
Requires:       libsoup
Requires:       mutter
Requires:       pango
Requires:       python3dist(pygobject)
Provides:       gnome-tweak-tool = %{version}-%{release}
BuildArch:      noarch

%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.


%prep
%autosetup -n %{name}-%{tarball_version} -p1 -S gendiff


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/*.appdata.xml


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/%{name}
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{python3_sitelib}/gtweak/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.tweaks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
%{_datadir}/metainfo/*.appdata.xml


%changelog
* Mon Mar 14 2022 Milan Crha <mcrha@redhat.com> - 40.10-1
- Resolves: #2063688 (Update to 40.10 release)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 40.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 19 2021 Milan Crha <mcrha@redhat.com> - 40.0-5
- Resolves: #1973391 (Remove the patch, not applicable due to Nautilus changes)

* Fri Jun 18 2021 Milan Crha <mcrha@redhat.com> - 40.0-4
- Resolves: #1973391 (Backport downstream patch from older RHEL)

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 40.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Sat Mar 27 2021 Kalev Lember <klember@redhat.com> - 40.0-2
- Use upstream appdata screenshots

* Sat Mar 27 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Tue Feb 23 2021 Kalev Lember <klember@redhat.com> - 40~beta-4
- Require gnome-themes-extra for gtk3 css files

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-3
- Use same pre-release system as in other GNOME packages

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-2
- Require libhandy1 instead of libhandy

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 40~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.34.0-5
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-4
- Fix extension preferences opening (RHBZ #1820396)

* Sat Mar 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-3
- Add dependency on gnome-extensions-app (RHBZ #1812779)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.90-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.32.0-2
- Fix typo in Provides version (RHBZ #1721864)

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Wed Dec 19 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2
- Fix opening system installed extensions in gnome-software

* Fri Sep 28 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.30.0-1
- Update to 3.30.0

* Wed Aug 29 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.92-1
- Update to 3.29.92

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.91.1-1
- Update to 3.29.91.1

* Fri Aug 03 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.90.1-1
- Update to 3.29.90.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.29.2-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.2-1
- Update to 3.29.2

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.27.92-1
- Initial RPM release, based on gnome-tweak-tool.spec
