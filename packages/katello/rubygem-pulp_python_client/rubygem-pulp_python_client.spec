# template: default
%global gem_name pulp_python_client

Name: rubygem-%{gem_name}
Version: 3.6.1
Release: 1%{?dist}
Summary: Pulp 3 API Ruby Gem
License: GPLv2+
URL: https://github.com/pulp/pulp_python
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9
BuildRequires: ruby >= 1.9
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Fetch, Upload, Organize, and Distribute Software Packages.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%exclude %{gem_instdir}/pulp_python_client.gemspec
%{gem_instdir}/spec

%changelog
* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.6.1-1
- Update to 3.6.1

* Thu Apr 07 2022 ianballou <ianballou67@gmail.com> 3.6.0-1
- Update to 3.6.0

* Wed Oct 06 2021 Justin Sherrill <jsherril@redhat.com> 3.5.2-1
- Update to 3.5.2

* Tue Jul 06 2021 James Jeffers <jjeffers@redhat.com> 3.4.0-1
- Update to 3.4.0

* Tue Jun 15 2021 ianballou <ianballou67@gmail.com> 3.2.0-1
- Add rubygem-pulp_python_client generated by gem2rpm using the scl template
