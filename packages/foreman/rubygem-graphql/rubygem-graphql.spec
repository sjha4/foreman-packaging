# template: default
%global gem_name graphql

Name: rubygem-%{gem_name}
Version: 1.13.16
Release: 1%{?dist}
Summary: A GraphQL language and runtime for Ruby
License: MIT
URL: https://github.com/rmosolgo/graphql-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4.0
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A plain-Ruby implementation of GraphQL.


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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/readme.md
%{gem_instdir}/spec

%changelog
* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.13.16-1
- Update to 1.13.16

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.8.18-1
- Update to 1.8.18

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.14-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.14-2
- Bump to release for EL8

* Wed Feb 13 2019 Ondrej Prazak <oprazak@redhat.com> 1.8.14-1
- Add rubygem-graphql generated by gem2rpm using the scl template
