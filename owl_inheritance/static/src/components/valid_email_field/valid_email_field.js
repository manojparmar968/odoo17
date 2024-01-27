/** @odoo-module */

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { EmailField } from "@web/views/fields/email/email_field";

class ValidEmailField extends EmailField {
    setup(){
        super.setup()
        console.log("Email Field Inherited")
        // console.log(this.props)
    }

    get isValidEmail(){
        let re = /\S+@\S+\.\S+/;
        // return re.test(this.props.value)
    }
};

// ValidEmailField.template = "owl.ValidEmailField"
ValidEmailField.supportedTypes = ["char"]
ValidEmailField.displayName= _t("Email")

registry.category("fields").add("valid_email", ValidEmailField);