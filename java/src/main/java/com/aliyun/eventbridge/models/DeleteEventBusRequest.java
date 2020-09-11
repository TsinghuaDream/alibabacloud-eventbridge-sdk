// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.eventbridge.models;

import com.aliyun.tea.NameInMap;
import com.aliyun.tea.TeaModel;
import com.aliyun.tea.Validation;

/**
 * The request of delete the EventBus
 */
public class DeleteEventBusRequest extends TeaModel {
    @NameInMap("EventBusName")
    @Validation(required = true)
    public String eventBusName;

    public static DeleteEventBusRequest build(java.util.Map<String, ?> map) {
        DeleteEventBusRequest self = new DeleteEventBusRequest();
        return TeaModel.build(map, self);
    }

    public DeleteEventBusRequest setEventBusName(String eventBusName) {
        this.eventBusName = eventBusName;
        return this;
    }

    public String getEventBusName() {
        return this.eventBusName;
    }

}
