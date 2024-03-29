# diSimplicial expositional base website project

This project contains the base sub-website for the diSimplex exposition
website.

# Licences and Prior Art

The diSimplex expositional website projects individually and collectively
contain a mixture of exposition, discussion as well as working compilable
or interpretable code. As such the contents of these projects are licensed
for use under the dual Creative Commons BY-SA 4.0 license for any non-code
artefacts, as well as the Apache 2.0 license for any code artefacts.

In addition any and all new patentable ideas contained in the contents of
any of the diSimplex website projects, are meant to document Prior Art from
the time they are commited in a publicly accessible version control archive
(such as, but not restricted to, GitHub).

Finally, both the CC-BY-SA 4.0 License (section 5), and the Apache 2.0
License (sections 7 and 8) contain Disclaimers of Warranties and
Limitations of Liability. These disclaimers and limitiations apply either
singly or collectively to the whole of any diSimplex website project.

For details see the attached

   [Licenses and Prior Art](_LicensesAndPriorArt.md)

## Comment form

I would like to have [OrcID](https://orcid.org/)
[authentication](https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/#easy-faq-12511).

OrcID suggests that this can be done completely in JavaScript in the
user's browser using the [OrcID JavaScript
Widget](https://github.com/ORCID/orcid-auth-widget).

It looks like this should work. The comment collector will archive the
headers which will contain the verified OrcID token. The comment processor
can then use this OrcID token to verify that the user is a valid user.

NOTE: the form MUST also contain the user's email address....

Then the comment processor could keep a database of the User's name and
OrcID (from OrcID), as well as their email (from the user and verified
automagically/by-hand).
