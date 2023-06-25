# template: default
%global gem_name scoped_search

Name: rubygem-%{gem_name}
Version: 4.1.11
Release: 1%{?dist}
Summary: Easily search you ActiveRecord models with a simple query language using a named scope
License: MIT
URL: https://github.com/wvanbergen/scoped_search/wiki
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Scoped search makes it easy to search your ActiveRecord-based models.
It will create a named scope :search_for that can be called with a query
string. It will build an SQL query using
the provided query string and a definition that specifies on what fields to
search. Because the functionality is
built on named_scope, the result of the search_for call can be used like any
other named_scope, so it can be
chained with another scope or combined with will_paginate.
Because it uses standard SQL, it does not require any setup, indexers or
daemons. This makes scoped_search
suitable to quickly add basic search functionality to your application with
little hassle. On the other hand,
it may not be the best choice if it is going to be used on very large datasets
or by a large user base.


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
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/CONTRIBUTING.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.activerecord42
%{gem_instdir}/Gemfile.activerecord50
%{gem_instdir}/Gemfile.activerecord51
%{gem_instdir}/Gemfile.activerecord52
%{gem_instdir}/Gemfile.activerecord52_with_activesupport52
%{gem_instdir}/Gemfile.activerecord60
%{gem_instdir}/Gemfile.activerecord60_with_activesupport60
%{gem_instdir}/Gemfile.activerecord61
%{gem_instdir}/Gemfile.activerecord61_with_activesupport61
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/scoped_search.gemspec
%{gem_instdir}/spec

%changelog
* Sun Jun 25 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.1.11-1
- Update to 4.1.11

* Mon Nov 29 2021 Adam Ruzicka <aruzicka@redhat.com> 4.1.10-1
- Update to 4.1.10

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.1.9-2
- Rebuild against rh-ruby27

* Mon Aug 24 2020 Adam Ruzicka <aruzicka@redhat.com> 4.1.9-1
- Update to 4.1.9

* Wed Apr 15 2020 Adam Ruzicka <aruzicka@redhat.com> 4.1.8-1
- Update to 4.1.8

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.7-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.1.7-2
- Update spec to remove the ror scl

* Tue May 07 2019 Marek Hulan <mhulan@redhat.com> 4.1.7-1
- Update to 4.1.7

* Wed Nov 21 2018 Marek Hulan <mhulan@redhat.com> 4.1.6-1
- Update to 4.1.6

* Wed Sep 19 2018 Marek Hulan <mhulan@redhat.com> 4.1.5-1
- Update to 4.1.5

* Thu Sep 06 2018 Marek Hulan <mhulan@redhat.com> 4.1.4-1
- Update to 4.1.4

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.1.3-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.1.2-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Sep 08 2017 Daniel Lobato Garcia <me@daniellobato.me> 4.1.2-1
- Update scoped_search to 0.4.2 (ares@users.noreply.github.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Mar 29 2017 Dominic Cleal <dominic@cleal.org> 4.1.0-1
- Update scoped_search to 4.1.0 (dominic@cleal.org)

* Mon Dec 19 2016 Dominic Cleal <dominic@cleal.org> 4.0.0-1
- Update scoped_search to 4.0.0 (dominic@cleal.org)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 3.3.0-1
- Update scoped_search to 3.3.0 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 3.2.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.2.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.2.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 3.2.2-1
- Update scoped_search to 3.2.2 (dcleal@redhat.com)

* Wed Jun 24 2015 Dominic Cleal <dcleal@redhat.com> 3.2.1-1
- Update scoped_search to 3.2.1 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 3.2.0-2
- Fix ruby(abi) requirement on F19 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 3.2.0-1
- Update scoped_search to 3.2.0 (dcleal@redhat.com)

* Mon Mar 24 2014 Dominic Cleal <dcleal@redhat.com> 2.7.1-1
- rebase to 2.7.1 release (dcleal@redhat.com)

* Mon Mar 10 2014 Dominic Cleal <dcleal@redhat.com> 2.6.5-1
- rebase to 2.6.5 release (dcleal@redhat.com)

* Wed Feb 12 2014 Dominic Cleal <dcleal@redhat.com> 2.6.3-1
- rebase to 2.6.3 release (dcleal@redhat.com)

* Mon Feb 10 2014 Dominic Cleal <dcleal@redhat.com> 2.6.2-1
- rebase to 2.6.2 release (dcleal@redhat.com)

* Thu Jun 20 2013 Miroslav Suchý <msuchy@redhat.com> 2.6.0-1
- rebase to 2.6.0 release (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-3
- fix files section (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-2
- fix files section (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-1
- rebase to scoped_search 2.5.1 (msuchy@redhat.com)

* Tue Apr 02 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.0-1
- rebase to scoped_search-2.5.0 (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-3
- include vendor in file list (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-2
- include assets in file list (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-1
- rebase to scoped_search-2.4.1 (msuchy@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.0-6
- new package built with tito

* Mon Dec 03 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-5
- run test only on F18+ (msuchy@redhat.com)
- enable tests (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-4
- do not run test on rhel6 at all due missing rspec (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-3
- remove .travis.yml, add Gemfile.activerecord* (msuchy@redhat.com)

* Mon Oct 29 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-2
- do not run test, because it is not working (msuchy@redhat.com)
- disable testing on other backend but sqllite (msuchy@redhat.com)
- update to recent scoped_search-2.4.0.gem (msuchy@redhat.com)

* Tue Oct 16 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-1
- update to recent scoped_search-2.4.0.gem (msuchy@redhat.com)

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-10
- 847504 - move gemspec to -doc subpackage (msuchy@redhat.com)

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-9
- test suite is failing on F17 a lot - disable for now (msuchy@redhat.com)
- 847504 - use test suite (msuchy@redhat.com)
- 847504 - remove dot files in %%install section (msuchy@redhat.com)
- 847504 - use macro in SOURCE0 (msuchy@redhat.com)

* Tue Aug 14 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-8
- 847504 - put in front of chmod link to github issue (msuchy@redhat.com)
- 847504 - fix typo in summary (msuchy@redhat.com)

* Tue Aug 14 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-7
- 847504 - remove cached gem (msuchy@redhat.com)
- 847504 - correctly use dist tag (msuchy@redhat.com)
- 847504 - rewrap description (msuchy@redhat.com)

* Sun Aug 12 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-6
- fix spelling error (msuchy@redhat.com)
- module scoped_search.rb should not be executable (msuchy@redhat.com)

* Sun Aug 12 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-5
- buildroot is not needed (msuchy@redhat.com)
- change Group to valid item (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-4
- there is no need to require rubygems in some version (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-3
- there is no need to require rubygems in some version (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-2
- fix filelist (msuchy@redhat.com)
- create doc subpackage (msuchy@redhat.com)
- fix requirements (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-1
- edit rubygem-scoped_search.spec according guidelines (msuchy@redhat.com)
- import rubygem-scoped_search.spec from foreman-rpms (msuchy@redhat.com)
