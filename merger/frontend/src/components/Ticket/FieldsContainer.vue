<template>
    <div>
        <form action="">
            <div v-if="content.type_field === 'text_field'" class="custom-model-container">
                <label :for="content.lable">{{ content.lable }}</label>
                <input type="text" class="input-text" :name="content.lable" :placeholder="content.placeholder" v-model="formInpuit" @input="emitValue()">
            </div>

            <div v-else-if="content.type_field == 'text_area'" class="custom-model-container">
                <label :for="content.lable">{{ content.lable }}</label>
                <textarea class="text-area" :name="content.lable" :placeholder="content.placeholder" :rows="content.rows" :cols="content.cols" v-model="formInpuit" @input="emitValue()"></textarea>
            </div>

            <div v-else-if="content.type_field == 'ceck_box'" class="custom-model-container ceckbox">
                <label :for="content.lable">{{ content.lable }}</label>
                <input type="checkbox" class="ceck-box" :name="content.lable" :placeholder="content.placeholder" v-model="formInpuit" @input="emitValue()"/>
            </div>

            <div v-else-if="content.type_field == 'group_ceckbox'" class="custom-model-container">
                <label :for="content.lable">{{ content.lable }}</label>
                <div v-for="item in grupInpuitCeckbox" :key="item.id" class="custom-group-input">
                    <label :for="item.label">
                        <input type="checkbox"  :name="item.lable" :value="item.value" v-model="item.state" @input="emitValue('ceckbox')">
                        {{ item.lable }}
                    </label>
                </div>
            </div>

            <div v-else-if="content.type_field == 'group_dropdown'" class="custom-model-container">
                <label :for="content.lable">{{ content.lable }}</label>
                <div v-for="item in content.input_group_dropdown" :key="item.id">
                    {{ item }}
                </div>
            </div>

            <div v-else-if="content.type_field == 'group_radio'" class="custom-model-container">
                <label :for="content.lable">{{ content.lable }}</label>
                <div v-for="item in content.input_group_radiogroup" :key="item" class="custom-group-input">
                    <input v-model="grupInpuitRadio" type="radio" :name="item.lable" :value="item.value"  @input="emitValue('radio')">
                    <label :for="content.lable">
                        {{ item.lable }}
                    </label>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        content: {
            type: Object,
            required: true
        }
    },
    data () {
        return {
            formInpuit : this.content.vlaue,
            grupInpuitCeckbox : this.generateGrupInpuitCeckbox(),
            grupInpuitRadio : undefined
        }
    },
    methods: {
        emitValue: function (input) {
            

            if (input == 'ceckbox') {
                
                this.$emit("input-change", {
                    modelId : this.content.id,
                    primary_key : this.content.primary_key,
                    field : this.content.type_field,
                    value : this.grupInpuitCeckbox,
                });
            } else if (input == 'radio') {
                console.log(this.grupInpuitRadio)
                this.$emit("input-change", {
                    modelId : this.content.id,
                    primary_key : this.content.primary_key,
                    field : this.content.type_field,
                    value : this.grupInpuitRadio,
                });
            } else {
                this.$emit("input-change", {
                    modelId : this.content.id,
                    primary_key : this.content.primary_key,
                    field : this.content.type_field,
                    value : this.formInpuit,
                });
            }
        },
        generateGrupInpuitCeckbox : function () {
            if (this.content.input_group_ceckbox) {
                const result = []
                this.content.input_group_ceckbox.forEach(element => {
                    element.state = false
                    result.push(element)
                });
                return result
            }
            return undefined
        }
    }
}
</script>

<style scoped lang="scss">

.custom-model-container {
    position: relative;
    display: flex;
    flex-direction: column;
    margin: 0.5rem;

    &.ceckbox{
        flex-direction: row;
        align-items: baseline; 
    }

    label {
        margin: 1rem 0 0.5rem 0;
        font-weight: 600;
        font-size: 1.2rem;
    }

    Textarea.text-area {
        padding: .5rem .5rem;
        border-radius: 8px;
        border: 1px solid #313131;
    }

    input.input-text {
        padding: .5rem .5rem;
        border-radius: 8px;
        border: 1px solid #313131;
    }

    input.ceck-box{
        margin-left: .5rem;
        scale: 120%;
    }

    .custom-group-input{

        label {
            margin: 1rem 0 0.5rem 0;
            font-weight: 500;
            font-size: 1rem;
            margin-left: .25rem;
        }
    }
}

</style>