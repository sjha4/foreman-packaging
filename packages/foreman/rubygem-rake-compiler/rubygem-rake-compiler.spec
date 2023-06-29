# template: default
%global gem_name rake-compiler

Name: rubygem-%{gem_name}
Version: 1.2.3
Release: 1%{?dist}
Summary: Rake-based Ruby Extension (C, Java) task generator
License: MIT
URL: https://github.com/rake-compiler/rake-compiler
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.8.7
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems-devel >= 1.8.23
BuildArch: noarch
# end specfile generated dependencies

%description
Provide a standard and simplified way to build and package
Ruby extensions (C, Java) using Rake as glue.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rake-compiler
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/appveyor.yml
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber.yml
%{gem_instdir}/features

%changelog
* Thu Jun 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.3-1
- Update to 1.2.3

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.2.1-1
- Update to 1.2.1

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.2.0-1
- Update to 1.2.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.7-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.7-3
- Bump to release for EL8

* Tue Oct 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.7-2
- Update and rebuild into SCL

* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 1.0.7-1
- Add rubygem-rake-compiler generated by gem2rpm using the scl template

