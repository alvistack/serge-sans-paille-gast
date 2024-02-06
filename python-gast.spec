# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-gast
Epoch: 100
Version: 0.5.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Python AST that abstracts the underlying Python version
License: BSD-3-Clause
URL: https://github.com/serge-sans-paille/gast/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree
(AST). GAST provides a compatibility layer between the AST of various
Python versions, as produced by ast.parse from the standard ast module.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-gast
Summary: Python AST that abstracts the underlying Python version
Requires: python3
Provides: python3-gast = %{epoch}:%{version}-%{release}
Provides: python3dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gast) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gast
A generic AST to represent Python2 and Python3's Abstract Syntax Tree
(AST). GAST provides a compatibility layer between the AST of various
Python versions, as produced by ast.parse from the standard ast module.

%files -n python%{python3_version_nodots}-gast
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-gast
Summary: Python AST that abstracts the underlying Python version
Requires: python3
Provides: python3-gast = %{epoch}:%{version}-%{release}
Provides: python3dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gast) = %{epoch}:%{version}-%{release}

%description -n python3-gast
A generic AST to represent Python2 and Python3's Abstract Syntax Tree
(AST). GAST provides a compatibility layer between the AST of various
Python versions, as produced by ast.parse from the standard ast module.

%files -n python3-gast
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-gast
Summary: Python AST that abstracts the underlying Python version
Requires: python3
Provides: python3-gast = %{epoch}:%{version}-%{release}
Provides: python3dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gast) = %{epoch}:%{version}-%{release}

%description -n python3-gast
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python3-gast
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
