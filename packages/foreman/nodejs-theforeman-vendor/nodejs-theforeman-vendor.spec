%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @theforeman/vendor

Name: %{?scl_prefix}nodejs-theforeman-vendor
Version: 10.1.0
Release: 1%{?dist}
Summary: foreman supported 3rd-party node_modules
License: MIT
Group: Development/Libraries
URL: https://github.com/theforeman/foreman-js#readme
Source0: https://registry.npmjs.org/@theforeman/vendor/-/vendor-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr scss %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc CHANGELOG.md
%doc docs
%doc readme.md

%changelog
* Mon Feb 21 2022 vagrant 10.1.0-1
- Update to 10.1.0

* Tue Jan 18 2022 MariaAga <mariaaga@redhat.com> 10.0.0-1
- Update to 10.0.0

* Thu Oct 21 2021 Ron Lavi <1ronlavi@gmail.com> 8.16.0-1
- Update to 8.16.0

* Wed Oct 06 2021 Ron Lavi <1ronlavi@gmail.com> 8.15.0-1
- Update to 8.15.0

* Tue Jul 13 2021 Tomer Brisker <tbrisker@gmail.com> 8.8.0-1
- Update to 8.8.0

* Wed Jun 30 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 8.7.0-1
- Update to 8.7.0

* Fri Apr 30 2021 Evgeni Golov 8.4.5-1
- Update to 8.4.5

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> 8.4.1-1
- Update to 8.4.1

* Tue Feb 16 2021 Ondrej Prazak <oprazak@redhat.com> 8.3.3-1
- Update to 8.3.3

* Tue Feb 09 2021 Ondrej Prazak <oprazak@redhat.com> 8.3.0-1
- Update to 8.3.0

* Tue Nov 17 2020 John Mitsch <jomitsch@redhat.com> 6.0.0-1
- Update to 6.0.0

* Tue Aug 18 2020 Avi Sharvit <sharvita@gmail.com> 4.14.0-1
- Update to 4.14.0

* Tue Jul 28 2020 MariaAga <mariaagaphonchev@gmail.com> 4.12.0-1
- Update to 4.12.0

* Thu Jul 09 2020 Avi Sharvit <sharvita@gmail.com> 4.11.1-1
- Update to 4.11.1

* Sun Jun 21 2020 Avi Sharvit <sharvita@gmail.com> 4.8.0-1
- Update to 4.8.0

* Sun Apr 26 2020 Avi Sharvit <sharvita@gmail.com> 4.5.0-1
- Update to 4.5.0

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.3.0-2
- Bump packages to build for el8

* Fri Apr 03 2020 Evgeni Golov 4.3.0-1
- Update to 4.3.0

* Mon Jan 27 2020 Tomer Brisker <tbrisker@gmail.com> 4.0.7-1
- Update to 4.0.7

* Tue Jan 07 2020 Avi Sharvit <sharvita@gmail.com> 4.0.2-1
- Update to 4.0.2

* Tue Dec 17 2019 Evgeni Golov 3.9.0-1
- Update to 3.9.0

* Tue Dec 17 2019 Evgeni Golov 3.8.1-1
- Update to 3.8.1

* Sat Dec 07 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.5.2-1
- Update to 3.5.2

* Mon Dec 02 2019 Evgeni Golov 3.3.2-1
- Update to 3.3.2

* Mon Dec 02 2019 Evgeni Golov 3.3.1-1
- Update to 3.3.1

* Wed Nov 27 2019 Evgeni Golov 3.3.0-1
- Update to 3.3.0

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-2
- Update specs to handle SCL

* Tue Sep 24 2019 Ondřej Ezr <oezr@redhat.com> 1.7.0-1
- Update to 1.7.0

* Tue Aug 20 2019 Avi Sharvit <sharvita@gmail.com> 1.4.0-1
- Update to 1.4.0

* Tue Jul 23 2019 Evgeni Golov 0.1.1-1
- Update to 0.1.1

* Tue Jul 16 2019 Evgeni Golov 0.1.0-0.1.alpha.11
- Add nodejs-theforeman-vendor generated by npm2rpm using the single strategy
