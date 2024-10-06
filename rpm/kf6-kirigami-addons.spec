%global  kf_version 6.6.0

Name:           kf6-kirigami-addons
Version:        1.4.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source0: %{name}-%{version}.tar.bz2

Patch0: 0001-Drop-requirement-on-GlobalAccel.patch

BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ksvg-devel

BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Provides:  kf6-kirigami2-addons = 1:%{version}-%{release}
Provides:  kf6-kirigami2-addons%{?_isa} = 1:%{version}-%{release}

# ### Merged subpackages back into main package
# # The old name
# Obsoletes: kf6-kirigami2-addons-dateandtime < 1:0.11.76-5
# Provides:  kf6-kirigami2-addons-dateandtime = 1:%{version}-%{release}
# Provides:  kf6-kirigami2-addons-dateandtime%{?_isa} = 1:%{version}-%{release}

# Obsoletes: kf6-kirigami2-addons-treeview < 1:0.11.76-5
# Provides:  kf6-kirigami2-addons-treeview = 1:%{version}-%{release}
# Provides:  kf6-kirigami2-addons-treeview%{?_isa} = 1:%{version}-%{release}

# # The new name
# Obsoletes: kf6-kirigami-addons-dateandtime < 0.11.76-5
# Provides:  kf6-kirigami-addons-dateandtime = %{version}-%{release}
# Provides:  kf6-kirigami-addons-dateandtime%{?_isa} = %{version}-%{release}

# Obsoletes: kf6-kirigami-addons-treeview < 0.11.76-5
# Provides:  kf6-kirigami-addons-treeview = %{version}-%{release}
# Provides:  kf6-kirigami-addons-treeview%{?_isa} = %{version}-%{release}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Conflicts: kf6-kirigami-addons < 1.4.0
%description devel
The %{name}-devel package contains CMake definitions, libraries
and header files for developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/
%dir %{_kf6_qmldir}/org/kde
%{_kf6_qmldir}/org/kde/kirigamiaddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.{6,%{version}}

%files devel
%{_kf6_libdir}/cmake/KF6KirigamiAddons
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
