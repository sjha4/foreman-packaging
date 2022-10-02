# template: default
%global gem_name msgpack
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.5.6
Release: 1%{?dist}
Summary: MessagePack, a binary-based efficient data interchange format
License: Apache 2.0
URL: https://msgpack.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4
BuildRequires: ruby-devel >= 2.4
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/appveyor.yml
%{gem_instdir}/bench
%{gem_libdir}
%{gem_instdir}/msgpack.org.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doclib
%{gem_instdir}/msgpack.gemspec
%{gem_instdir}/spec

%changelog
* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.5.6-1
- Update to 1.5.6

* Sun Jul 31 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.5.4-1
- Update to 1.5.4

* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.5.3-1
- Update to 1.5.3

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.3-2
- Rebuild for Ruby 2.7

* Thu Jul 09 2020 Bernhard Suttner <suttner@atix.de> 1.3.3-1
- Add rubygem-msgpack generated by gem2rpm using the scl template

