# Created by pyp2rpm-3.3.3
%global pypi_name pulp-2to3-migration

Name:           python-%{pypi_name}
Version:        0.2.0b1
Release:        1%{?dist}
Summary:        Pulp 2 to Pulp 3 migration tool

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pulpcore >= 3.1
BuildRequires:  python3-jsonschema
BuildRequires:  python3-mongoengine
BuildRequires:  python3-semantic_version
BuildRequires:  python3-setuptools

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pulpcore >= 3.1
Requires:       python3-jsonschema
Requires:       python3-mongoengine
Requires:       python3-semantic_version
Requires:       python3-setuptools
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/pulp_2to3_migration
%{python3_sitelib}/pulp_2to3_migration-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 25 2020 Samir Jha <sjha4@ncsu.edu> - 0.2.0b1-1
- Initial package.
