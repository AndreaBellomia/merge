<template>
    <div>
        <div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true" :class="`${popUp ? '' : 'hidden'}`">
            <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
            <div class="fixed inset-0 z-10 overflow-y-auto">
                <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                    <div v-if="popUpState">
                        <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                            
                                <div class="sm:flex sm:items-start" >
                                    <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                                    <!-- Heroicon name: outline/exclamation-triangle -->
                                    <span class="material-icons">
                                        delete
                                    </span>
                                    </div>
                                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                    <h3 class="text-lg font-medium leading-6 text-gray-900" id="modal-title">Cancella Appuntamento</h3>
                                    <div class="mt-2">
                                        <p>Sei sicuro di voler cancellare l'appuntamento ?</p>
                                    </div>
                                    </div>
                                </div>
                        </div>
                        <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                            <button @click="$emit('deleteModal', popUpId.id)" type="button" class="inline-flex w-full justify-center rounded-md border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm">Elimina</button>
                            <button @click="$emit('closeModal')" type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">Annulla</button>
                        </div>
                    </div>
                    <div v-else>
                        <div class="bg-white px-4 pt-5 pb-4 p-6 pb-4">
                            
                                <div class="flex flex-col items-center p-1" >
                                    <div class="mx-auto flex p-8 flex-shrink-0 items-center justify-center rounded-full bg-green-100 h-10 w-10">
                                        <span class="material-icons scale-150">
                                            done
                                        </span>
                                    </div>
                                    <div class="mt-2 text-center sm:mt-0 ml-4 text-left pt-5">
                                    <h3 class="text-lg font-medium leading-6 text-gray-900" id="modal-title">Callazione Avvenuta!</h3>
                                    <div class="mt-2">
                                        <p>La cancellazione dell'appuntamento è avvenuta con successo!</p>
                                    </div>
                                    </div>
                                </div>
                        </div>
                        <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                            <button @click="$emit('closeModal')" type="button" class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-base font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">Chiudi</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        </div>
    </div>
</template>


<script>
export default {
    props: {
        popUpId: {
            type: [Object, Function]
        },
        popUpState: {
            type: Boolean,
            required: true
        },
        popUp: {
            type: Boolean,
            required: true
        }
    }
}
</script>